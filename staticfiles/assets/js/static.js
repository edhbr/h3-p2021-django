const _glob = require("glob");

/**
 * Get a files glob
 * @param {string} path - file path
 * @param {boolean} onlyFileName - return only the file name
 * @return {array} - glob
 */
const glob = (path, onlyFileName = false) => {
  const result = _glob.sync(path, { nodir: true });
  return onlyFileName ? result.map(i => getFileRoute(i)) : result;
};

/**
 * Get the file route
 * @param {string} str - file full path
 * @return {string} - file route
 */
const getFileRoute = str => {
  return str.replace(/(\.content\/[\w-_]*\/|\.\w+$)/g, "");
};

/**
 * Get the file name
 * @param {string} str - file full path
 * @return {string} - file name
 */
const getFileName = str => {
  return getFileRoute(str).replace(/^[\w-_]*\//g, "");
};

/**
 * Nuxt generated router for static cms
 * @return {array} - generated router
 */
const generateStaticRoutes = () => {
  const routes = [];

  // CMS posts content
  const posts = getPosts();
  routes.push(...posts);

  // CMS pages content
  routes.push(
    ...glob(".content/pages/**/*.json", true).filter(i => i !== "index")
  );

  return routes;
};

/**
 * Get an array of posts
 * @param {string} type - posts type to match
 * @param {array} fields - key to return in payload
 * @param {boolean} onlyPayload - include only payload in returned array
 * @return {array} - requested posts
 */
const getPosts = (type = "**", fields = [], onlyPayload = false) => {
  const posts = glob(`.content/posts/${type}/*.json`);

  const result = [];

  for (const post of posts) {
    const data = require(`../../${post}`);
    const temp = {
      route: getFileRoute(post),
      payload: {
        route: getFileRoute(post),
        slug: getFileName(post)
      }
    };

    if (fields.length) {
      for (const field of fields) {
        temp.payload[field] = data[field];
      }
    } else {
      temp.payload = { ...temp.payload, ...data };
    }

    result.push(temp);
  }

  console.log(type, result);

  return onlyPayload ? result.map(i => i.payload) : result;
};

const blogPosts = getPosts(
  "blog",
  ["date", "title", "featured_image", "lead"],
  true
);

export { generateStaticRoutes, getPosts, blogPosts };
